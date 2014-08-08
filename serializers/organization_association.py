__author__ = 'valentin'

from tastypie.serializers import Serializer

from rdflib import Graph,Literal,BNode,Namespace,RDF,RDFS, URIRef, XSD

from rdflib.namespace import Namespace,DC,DCTERMS, FOAF
from rdflib import ConjunctiveGraph


class OrganizationAssociationFoafSerializer(Serializer):
    formats = ['json','jsonp','rdf']
    content_types = {
        'json':'application/json',
        'jsonp':'text/javascript',
        'rdf':'application/rdf+xml'

    }
    schemaOrg = Namespace('http://www.schema.org/')

# use schema.org to render a person, and an organizational role
# http://schema.org/OrganizationRole
    # or should this just be the OrganizationRole
    def to_rdf(self, data, options=None):
        org = data.obj.organization #uri is in data['organization'] or obj.resource_uri
        person = data.obj.person #uri is in data['data'] or obj.resource_uri

        data = self.to_simple(data, options)

        g = ConjunctiveGraph()
        g.bind('dc',DC)
        g.bind('dc',DCTERMS)
        g.bind('foaf',FOAF)
        g.bind('schema',self.schemaOrg)

        personGraph = Graph(g.store,FOAF.person)
        roleGraph  =   Graph(g.store,self.schemaOrg.OrganizationRole)

        #topNode = BNode()

        #topNode.set(RDF.type, FOAF.Person) # .set replaces all other values
        #topNode.set(RDFS.label, Literal("org2"))

        #topNode = URIRef(data['resource_uri'])

        if (data['person']):
            topNode = URIRef(data['person'])
            #personNode =URIRef(data['person'])
            personGraph.add( (topNode,RDF.type,FOAF.person) )
            personGraph.add( (topNode,FOAF.name,Literal( person.name )) )
            personGraph.add( (topNode,self.schemaOrg.sameas,URIRef(data['person'])))

        roleNode = URIRef(data['resource_uri'])
        roleGraph.add( (roleNode,RDF.type,self.schemaOrg.OrganizationRole) )


        if(data['jobTitle']):
            roleGraph.add( (roleNode,self.schemaOrg.namedPosition,Literal(data['jobTitle']) ) )

        if (data['organization']):
            roleGraph.add( (roleNode,self.schemaOrg.name,Literal( org.name) ) )
            roleGraph.add( (roleNode,self.schemaOrg.sameAs,URIRef(data['organization'])))

        if (data['beginDate']):
            roleGraph.add( (roleNode,self.schemaOrg.startDate,Literal(data['beginDate'],datatype=XSD.Date)))
        if (data['endDate']):
            roleGraph.add( (roleNode,self.schemaOrg.endData,Literal(data['beginDate'],datatype=XSD.Date)))


        # add role to person
        personGraph.add( (topNode, self.schemaOrg.memberOf,roleNode) )
        # if ( data['businessAddress'] ):
        #     g.add( (topNode,self.schemaOrg.address,Literal( data['businessAddress'] ) ) )

        # if(data['jobTitle']):
        #      g.add( (topNode,FOAF.homepage,URIRef(data['jobTitle'])) )



        # if( data['logoUrl']):
        #     g.add ( (topNode,FOAF.img, URIRef(data['logoUrl'])) )


        #g.add( (topNode,FOAF.nick,Literal("name",lang='en') ) )

        return g.serialize(format='xml')

    pass

