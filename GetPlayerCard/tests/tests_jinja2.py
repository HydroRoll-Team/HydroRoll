# -*- coding: utf-8 -*-

from jinja2 import Template

template = Template("hi, {{ username }}")
template.render(username="HsiangNianian")
print(template)
t = Template("{% set a, b = 'goo', '❄️' %}")
print(t, t.module.a)

from jinja2 import Environment, PackageLoader  # noqa: E402

env = Environment(loader=PackageLoader("get_pc", "templates"))
template = env.get_or_select_template("tests.template")
print(template.render(user="variables", go="here"))
