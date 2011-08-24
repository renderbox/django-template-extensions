from django.template import Library, Node, Variable, TemplateSyntaxError
from django.template.context import Context
from django.template.loader import render_to_string

register = Library()

class PartialsNode(Node):
    def __init__(self, template, key=None):
        self.template = template
        
        if key:
            self.key = Variable(key)
        else
            self.key = None
    
    def render(self, context):
        item = self.key.resolve(context)
        context = Context({ 'partial': item })
        return render_to_string(self.template, context )    # May need to make sure this is properly escaped

        # POSSIBE ALTERNATE WAY TO DO THIS
        #template = loader.get_template(self.template)
        #item = self.key.resolve(context)
        #context = Context({ 'partial': item })
        #return t.render(context)


@register.tag(name="partial")
def do_partial(parser, token):
    '''
    This tag will render a template with a context and include it back
    into the current template.  Good for creating consistent tables
    accross
    
    Syntax
    ----
    {% partial "partials/part.html" key %}
    
    '''
    bits = token.contents.split()
    if len(bits) < 2:
        raise TemplateSyntaxError, "partial renderer requires at least one argument, path to the partial template."
    
    if len(bits) > 3:
        raise TemplateSyntaxError, "partial renderer can not take more then two arguments, path to the partial template and a key to context value for rendering."

    if len(bits) == 2:
        return PartialsNode( bits[1] )

    return PartialsNode( bits[1], key=bits[2] )
