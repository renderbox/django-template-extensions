from django.utils.text import smart_split
# Token Parser

def advanced_split(token):
    '''
    advanced_split allows for positional and keyword arguments to be 
    used in template tags.  If commas are not being used, the more 
    traditional smart_split behavior is used (where it relies on spaces to 
    split on).
    
    Using the advanced split returns a tuple of (FILTER_NAME, ARGS, KWARGS).
    
    An example tag that can used the advanced_split would look like this:
    
    {{ filter bob, 1, foo = 10, phrase = "one two three"  }}
    
    same python rules for args coming before kwargs applies.
    '''
    
    args = []
    kwargs = {}
    onKWArgs = False
    
    contents = token.contents.split(',')
    
    if len(contents) == 1:                      # Return the default Django way.
        return token.contents.split()
        
    for i, c in enumerate(contents):
        temp = c.split("=")
        
        if i == 0:          # NEED TO STRIP OFF APP NAME FROM ARGS
            t = temp[0].split(" ")
            app = t[0]
            if len(t) > 1:
                temp[0] = " ".join(t[1:])
            else:
                temp[0] = ""
            
        if len(temp) > 1:
            onKWArgs = True
            kwargs[temp[0].strip()] = temp[1].strip()
            
        if len(temp) == 1:
            #if onKWArgs:
            #    raise exception
            args.append(temp[0].strip())
            
    return (app, args, kwargs)
