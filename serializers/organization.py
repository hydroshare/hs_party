__author__ = 'valentin'

from tastypie.serializers import Serializer

from rdflib import Graph,Literal,BNode,Namespace,RDF,RDFS, URIRef

from rdflib.namespace import DC,DCTERMS, FOAF

class OrganizationFFoafSerializer(Serializer):
    formats = ['json','jsonp','rdf']
    content_types = {
        'json':'application/json',
        'jsonp':'text/javascript',
        'rdf':'application/rdf+xml'

    }

    def to_rdf(self, data, options=None):
        data = self.to_simple(data, options)
        g = Graph()
        g.bind('dc',DC)
        g.bind('dc',DCTERMS)
        g.bind('foaf',FOAF)

        #org = BNode()
        org = URIRef(data['resource_uri'])
        #org.set(RDF.type, FOAF.Person) # .set replaces all other values
        #org.set(RDFS.label, Literal("org2"))

        g.add( (org,RDF.type,FOAF.organization) )
        g.add( (org,FOAF.nick,Literal("name",lang='en') ) )

        g.add( (org,FOAF.name,Literal("org2")) )
        g.add( (org,FOAF.mbox,URIRef("mailto:me@example.com")) )

        g.add( (org,DC.description,Literal("NOTE/BIO HERE") ) )
        g.add ( (org,FOAF.img, URIRef("http://www.example.com")) )

        return g.serialize(format='xml')

    pass

