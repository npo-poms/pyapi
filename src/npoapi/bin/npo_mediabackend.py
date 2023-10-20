#!/usr/bin/env python3
"""
  Simple client to get an object from the NPO Backend API media endpoint
"""
from npoapi import MediaBackend
from npoapi.base import Binding, DEFAULT_BINDING
from npoapi.xml import media_search
from xml.dom.minidom import parseString
import re

def mediabackend():
    client = MediaBackend().command_line_client(description="Set an media object from the NPO Backend API")
    client.add_argument('xml', type=str, nargs='?', help='The xml to post')
    client.add_argument('mid', type=str, nargs='?', help='The mid')
    list_of_subs = ["memberOf", ""]
    
    client.add_argument('sub', type=str, nargs='?', default="", choices=list_of_subs,
                        help="Sub call for the mediaobject. On default the mediaobject itself is returned, but you can also opt for one of these choices")
    
    client.add_argument('-S', '--search', action='store_true',
                       help="""Force that the xml is interpreted as a search""")
    client.add_argument('-W', '--writable', action='store_true',
                        help="""Only writable items are searched""")
    client.add_argument('-D', '--delete', action='store_true',
                       help="""The object with given mid will be deleted.""")
    
    client.add_argument('--raw', action='store_true', help="""The XML will not be parsed first. Implies that the argument is XML,  not a MID""")
    
    client.add_argument('--validate', action='store_true', help="""Use validateInput argument, when posting XML's.""")
    
    client.add_argument('--client_validate', action='store_true', help="""Make pyxb validate.""")
    
    client.add_argument('--steal_crids', type=str, default='IF_DELETED', help="""""", choices=['YES', 'NO', 'IF_DELETED'])
    
    client.add_argument('--lookup_crid', type=bool, help="""""", choices=[True, False])
    
    client.add_argument('-p', '--process', type=str,
                        help="""python code to postprocess. E.g.: 
                        update.midRef ='POMS_S_VPRO_168360'
                        """
                        )
    
    client.add_argument('-b', '--binding',
                        choices=Binding.__members__,
                        default=DEFAULT_BINDING.name,
                        help=""" 
                        binding to use when unmarshalling to objects (when using --process)
                        """
                        )
    
    
    args = client.parse_args()
    
    xml, mid, sub = args.xml, args.mid, args.sub
    
    binding = DEFAULT_BINDING if args.binding is None else Binding[args.binding.upper()]
    client.logger.debug("binding " + str(args.binding) + " " + str(binding))
    
    def is_prediction(update):
        if type(update) == str:
            return re.match("(<\?xml.*?>\s*)?<prediction\s", update)
        else:
            return update.childNodes[0].nodeName == "prediction"
    
    if args.delete:
        if mid is None:
            mid = xml
            xml = None
    
    
    if args.search:
        print(client.find(args.xml[0], writeable=args.writable))
    else:
        if xml:
            xmlString = client.data_or_from_file(xml)
            if args.raw:
                xml = xmlString
            else:
                xml = parseString(xmlString)
    
        if xml and not type(xml) == str and xml.childNodes[0].nodeName == "NPO_gfxwrp":
            if args.delete or args.search:
                client.exit("cannot delete or search parkpost")
            print(client.parkpost(xml))
        else:
            if xml:
                update = xml
                if args.process is not None:
                    update = client.to_object_or_none(xml, validate=args.client_validate, binding=binding)
                    exec(args.process)
                    client.logger.debug("Execed " + args.process)
                if not(type(update) == str) and xml.childNodes[0].namespaceURI == media_search.Namespace.uri():
                    if args.delete:
                        client.exit("cannot delete with search")
                    print(client.find(update, writable=args.writable, raw=args.raw, validate_input=args.validate, client_validate=args.client_validate))
                else:
                    if args.delete:
                        mid = update.mid
                        print(client.delete(mid))
                    else:
                        if is_prediction(update):
                            print(client.post(update, raw=args.raw, validate_input=args.validate, client_validate=args.client_validate, lookupcrid=args.lookup_crid))
                        else :
                            print(client.post(update,
                                              raw=args.raw,
                                              validate_input=args.validate, client_validate=args.client_validate, lookupcrid=args.lookup_crid, steal_crids=args.steal_crids, binding=binding, sub=args.sub, mid=mid))
            elif mid:
                if args.delete:
                    print(client.delete(mid))
                else:
                    print(client.get(mid))
    
    client.exit()
    
    

if __name__ == "__main__":
    mediabackend()
