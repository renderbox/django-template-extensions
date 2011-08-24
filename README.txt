Django Template Extensions (Alpha)

WARNING: This code is in an Alpha state, is untested and in flux, 
		 use at your own risk.  Don't build anything that depends heavily 
		 on it yet as somethings may change radically.

This is intended to be a series of useful extensions for the Django template system.
The initial push includes a template tag used for rendering partials.  A Partial is 
a template used to render a small chunk of html.  This is very useful in making 
consistently presented tables or template chunks that will get shares across
pages on a site.

You can accomplish a similar thing with "inclusion_tags" but they are a little more
complicated to set up.  Each tag in this case has to have special code written
for it.  The idea of the "partial" is the template and data to use are defined in
the template calling the partial as attributes passed in the tag.  This makes the
partial system more generic and easier to work with from a front end developer's
point of view.

EXAMPLE:

{% partial 'partials/foo.html' 'foo' %}

In this case the partial filter will look for the HTML template 'partials/foo.html'
and use the value from the context with the key 'foo'.  When the partial template 
gets rendered, the data gets repackaged into a new context with the key name 'partial'.

To use the data passed in the template you would access it with the key "partial"

{{ partial }}

The reasoning behind this is the same partial can be used multiple times in a single 
template render and so a more generic context variable name needs to be used for 
consistency and recyclability.