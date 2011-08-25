from django.utils.text import smart_split
# Token Parser

def advanced_split(token):
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
