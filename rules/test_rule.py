from durable.lang import *
import json
import jinja2
from pprint import pprint

# these rules would be from the rules database
# external-action is for the future when the consequent can trigger an orchestration via a rest/graphql API
rules_json = '''[
{
    "antecedent": "(m.id == 2) | (m.name == 'ok')",
    "consequent": {
        "disposition": "true positive",
        "auto-report": {"template_id": "t1" },
        "external-action": null
    }:q
:
},
{
    "antecedent": "(m.id == 3) | (m.name == 'poke')",
    "consequent": {
        "disposition": "true positive",
        "auto-report": {"template_id": "t2" },
        "external-action": null
    }

}
]
'''

# these templates would be from the reporting templates database
templates={ "t1": "findings: {{alert.name}}", "t2": "malware: {{alert.id}}" }

def process_consequent_actions(c, action_str, num):
    print("-----------\naction #" + str(num) + "\n-----------\n")
    actions = json.loads(action_str)
    alert = c.m

    for k,v in actions.items():
        if k=="disposition":
            print("setting disposition to " + v)
        elif k=="auto-report":
            template_id = v["template_id"]
            assert template_id in templates
            t = jinja2.Template(templates[template_id])
            print("sending report: " + t.render(alert=alert))
        else:
            print("unsupported action: " + k)

def gen_rule_str(rule, r):
#    rule_str=f'''
#@when_all({rule["antecedent"]})
#def action_{str(r)}(c):
#    print ('action_{str(r)}')
#'''
    rule_str='''
@when_all({0})
def action_{1}(c):
    process_consequent_actions(c, {2}, {1})
'''.format(rule["antecedent"], str(r), json.dumps(json.dumps(rule["consequent"])))
 
    return rule_str

def create_ruleset(ruleset_name, rules):
    r = 0
    with ruleset(ruleset_name):
        for rule in rules:
            #print(gen_rule_str(rule, r))
            exec(gen_rule_str(rule, r))
            r += 1
    
rules = json.loads(rules_json)

create_ruleset("expense", rules)
post('expense', { 'id': 1, 'name': 'ok'})    
post('expense', { 'id': 1, 'name': 'poke'})    

#t = jinja2.Template('hello {{alert.name}}')
#print(t.render(alert={"name": "world"}))

