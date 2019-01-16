import svgwrite
from xml.sax.handler import ContentHandler
from xml.sax import make_parser
from glob import glob
import svgwrite
import sys
import xml.etree.ElementTree as ET
tmp=0

cx=100
cy=100
longeur=400
largeur=600
coord=[]
class coordonnee():
    		def __init__(self,nomclasse,coordx,coordy):
			self.nomclasse=nomclasse
			self.coordx=coordx
			self.coordy=coordy
	#validation du fichier xml
def parsefile(file):
    parser = make_parser()
    parser.setContentHandler(ContentHandler())
    parser.parse(file)
file=sys.argv[1:]
for arg in file:
    for filename in glob(arg):
        try:
		parsefile(filename)
	except Exception as error:
		print(error)
		tmp=1
if tmp==0:
	class Classes():
    		def __init__(self,nomclasse,attribut,relation,attributrelation):
			self.nomclasse=nomclasse
			self.attribut=attribut
			self.relation=relation
			self.attributrelation=attributrelation
	clas=[]
	print("le fichier est bien forme")

	#Extraction du fichier xml
	tree = ET.parse(sys.argv[1])
	root = tree.getroot()
	entite=[]
	relation=[]
	element=[]
	attributr=[]
	i=0
	for child in root:
		entite.append(child.tag)

		for attribut in child:
			
			if attribut.tag=="enseigne" or attribut.tag=="Anime" :
			
				relation.append(attribut.tag)

				
			#else:
			element.append(attribut.tag)
			#print(attribut.tag)
			#print("-------------------")
			#print()
			for att in attribut:
				#print(att.tag)
				attributr.append(att.tag)
		clas.append(Classes(entite[i],element,relation,attributr))
		i+=1
		element=[]	
		valeur=[]
		
		attributr=[]
	for entite in clas:
	    print("-+---+---+---+---+---+")
	    print(entite.nomclasse)
	    print("-+---+---+---+---+---+-")
	    for attri in entite.attribut:
		print(attri)
	print("")
	print("-+---+---+---+---+---+")
	print("Relation")
	print("-+---+---+---+---+---+")
	for entite in relation:
	    
	    print(entite)
	print("-+---+---+---+---+---+")    
	    
else:
	print("le fichier n'est pas bien forme")
	

#generation du fichier xml

monClasse="Classes"
longueur=400
largeur=600
pointx=0
pointy=0
coinsx=longueur
coinsy=largeur

svg_document = svgwrite.Drawing(filename = "projet.svg",
								size = (longueur*5,largeur*5))

nbreattribut=0
def Tracer(clas):
    y=0
    entityCoords=[]
    entityCoordsList=[]
    for value in clas:
        # print(value.classe)
        # for value1 in value.attribut:
            # print(value1)
        # print("-------------+--------------------------------")

        if y%2 :
        	
            Cadrer(400*(y//2),600,value.nomclasse,value.attribut,len(value.attribut))
            coord.append(coordonnee(value.nomclasse,400*(y//2),600))
		    
	    	

            
        else:

            Cadrer(400*(y//2),100,value.nomclasse,value.attribut,len(value.attribut))
            coord.append(coordonnee(value.nomclasse,400*(y//2),100))
            
        y+=1
        

    print(svg_document.tostring())
    svg_document.save()
    


def Cadrer(cx,cy,nomclasse,attribut,nbreattribut):

    largeurp=largeur
    if nbreattribut>5:
        largeurp+=largeur*0.15*(nbreattribut-5)

    svg_document.add(svg_document.rect(insert = (cx, cy),
                                       size = (longeur-200, largeurp/3),
                                       stroke_width = "1",
                                       stroke = "black",
                                       fill = "rgb(0,255,255)"))

    svg_document.add(svg_document.text(nomclasse,
                                   textLength=110,
                                   insert = (50+cx,30+cy)))
    x=0;
    for value in attribut:

        svg_document.add(svg_document.text(value,
                                       insert = (longeur/10+cx, longeur/5+x+cy)))
        x+=25
   
    svg_document.add(svg_document.rect(insert = (cx, cy+50),
                                       size = (longeur-200,5),
                                       color= "black",
                                       stroke_width = "3",
                                       stroke = "black",
                                       fill = "rgb(255,0,255)"))
    
    
Tracer(clas)
