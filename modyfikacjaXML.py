from xml.dom.minidom import getDOMImplementation

with open('example.xml', 'r') as xmlFile:
    with open('return.xml', 'w') as toSave:
        for line in xmlFile:
            impl = getDOMImplementation()

            newdoc = impl.createDocument(None, "some_tag", None)
            top_element = newdoc.documentElement
            text = newdoc.createTextNode('Some textual content.')
            top_element.appendChild(text)