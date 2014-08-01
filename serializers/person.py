__author__ = 'valentin'

from tastypie.serializers import Serializer

from rdflib import Graph,Literal,BNode,Namespace,RDF, URIRef

from rdflib.namespace import DC,DCTERMS, FOAF

class PersonFoafSerializer(Serializer):
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

        person = URIRef(data['resource_uri'])
        g.add( (person,RDF.type,FOAF.person) )
        g.add( (person,FOAF.nick,Literal("name",lang='en') ) )

        g.add( (person,FOAF.name,Literal("Full Name")) )
        g.add( (person,FOAF.mbox,URIRef("mailto:me@example.com")) )
        g.add( (person,FOAF.givenName,Literal("first") ) )
        g.add( (person,FOAF.familyName,Literal("last") ) )
        g.add( (person,DC.description,Literal("NOTE/BIO HERE") ) )

        return g.serialize(format='xml')

    pass

