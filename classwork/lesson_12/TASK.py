def decorator_render(fune):
    def w(text):
        fune(text)
    return w
def render(text):
    print(text.upper())
# @decorator_render == peremennay = decorator_render(render)
@decorator_render
def render(text):
    print(text.upper())
render('hi')