"""
Patchless XMLRPC Service for Django
Kind of hacky, and stolen from Crast on irc.freenode.net:#django
Self documents as well, so if you call it from outside of an XML-RPC Client
it tells you about itself and its methods

Brendan W. McAdams <brendan.mcadams@thewintergrp.com>

SimpleXMLRPCDispatcher lets us register xml-rpc calls w/o
running a full XMLRPC Server.  It's up to us to dispatch data
"""
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from server.service import FooService
from SimpleXMLRPCServer import SimpleXMLRPCDispatcher


# Create a Dispatcher; this handles the calls and translates info to function maps
#dispatcher = SimpleXMLRPCDispatcher() # Python 2.4
dispatcher = SimpleXMLRPCDispatcher(allow_none=False, encoding=None)
# Support introspection, eg:'system.listMethods', 'system.methodHelp', 'system.methodSignature'
# http://pymotw.com/2/SimpleXMLRPCServer/
dispatcher.register_introspection_functions()


@csrf_exempt
def xmlrpc(request):
    """
    the actual handler:
    if you setup your urls.py properly, all calls to the xml-rpc service
    should be routed through here.
    If post data is defined, it assumes it's XML-RPC and tries to process as such
    Empty post assumes you're viewing from a browser and tells you about the service.

    :param request:
    :return:
    """
    if request.method == 'POST':
        response = HttpResponse(mimetype="application/xml")
        response.write(dispatcher._marshaled_dispatch(request.body))
    else:
        response = HttpResponse()
        response.write("<b>This is an XML-RPC Service.</b><br>")
        response.write("You need to invoke it using an XML-RPC Client!<br>")
        response.write("The following methods are available:<ul>")
        methods = dispatcher.system_listMethods()

        for method in methods:
                # right now, my version of SimpleXMLRPCDispatcher always
                # returns "signatures not supported"... :(
                # but, in an ideal world it will tell users what args are expected
                sig = dispatcher.system_methodSignature(method)

                # this just reads your docblock, so fill it in!
                help_txt = dispatcher.system_methodHelp(method)

                response.write("<li><b>%s</b>: [%s] %s" % (method, sig, help_txt))

        response.write("</ul>")

    response['Content-length'] = str(len(response.content))
    return response

# you have to manually register all functions that are xml-rpc-able with the dispatcher
# the dispatcher then maps the args down.
# The first argument is the actual method, the second is what to call it from the XML-RPC side...
dispatcher.register_instance(FooService())

