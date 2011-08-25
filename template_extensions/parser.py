from django.utils.text import smart_split
# Token Parser

def advanced_split(token):
    '''
    advanced_split allows for keyword arguments in addition to positional 
    arguments to be used in template tags.  If the '=>' key is used, this
    function will use the usual 'smart_split' and add some extra smarts 
    to when it comes accross the key.
    
    Using the advanced split returns a tuple of (FILTER_NAME, ARGS[], KWARGS{}).
    
    An example tag that can used the advanced_split would look like this:
    
    {% filter bob 1  foo => 10  phrase => "fifteen burgers" %}
    
    Same python rules for args coming before kwargs applies.
    
    The result will look like this:
    
    (u'filter', [u'bob', u'1'], {u'foo': u'10', u'phrase': u'"fifteen burgers"'})
    '''

    key = "=>"
    args = []
    kwargs = {}
    onKWArgs = False
    
    contents = list( smart_split(token.contents) )
    app = contents.pop(0)
    
    for i, c in enumerate(contents):
        
        if c == key:
            if not onKWArgs:
                args.pop()
                
            onKWArgs = True
            kwargs[ contents[ i - 1 ] ] = contents[ i + 1 ]
        elif not onKWArgs:
            args.append(c)
    
    return (app, args, kwargs)
