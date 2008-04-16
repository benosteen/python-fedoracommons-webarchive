

def createRoleList(name, selected=''):
    roles = {}
    roles[u"Author of afterword, colophon, etc."] = u"Author of afterword, colophon, etc."
    roles[u"Author in quotations or text abstracts"] = u"Author in quotations or text abstracts"
    roles[u"Author of introduction"] = u"Author of introduction"
    roles[u"Author"] = u"Author"
    roles[u"Collaborator"] = u"Collaborator"
    roles[u"Commentator"] = u"Commentator"
    roles[u"Creator"] = u"Creator"
    roles[u"Consultant"] = u"Consultant"
    roles[u"Consultant to a project"] = u"Consultant to a project"
    roles[u"Contributor"] = u"Contributor"
    roles[u"Commentator for written text"] = u"Commentator for written text"
    roles[u"Dubious author"] = u"Dubious author"
    roles[u"Originator"] = u"Originator"
    roles[u"Other"] = u"Other"
    roles[u"Owner"] = u"Owner"
    roles[u"Publisher"] = u"Publisher"
    roles[u"Performer"] = u"Performer"
    roles[u"Principal Investigator"] = u"Principal Investigator"
    roles[u"Researcher"] = u"Researcher"
    roles[u"Research team head"] = u"Research team head"
    roles[u"Research team member"] = u"Research team member"
    roles[u"Translator"] = u"Translator"
    roles[u"Writer of accompanying material"] = u"Writer of accompanying material"
    # Editing/reviewing roles
    roles[u"Adapter"] = u"Adapter"
    roles[u"Annotator"] = u"Annotator"
    roles[u"Compiler"] = u"Compiler"
    roles[u"Editor"] = u"Editor"
    roles[u"Reviewer"] = u"Reviewer"
    # Funder
    roles[u"Funder"] = u"Funder"
    # Copyright/etc roles
    roles[u"Process contact"] = u"Process contact"
    roles[u"Submitter"] = u"Submitter"
    roles[u"Former owner"] = u"Former owner"
    roles[u"Copyright holder"] = u"Copyright holder"
    
    if name == None or name == '':
        name = u'role1'
    
    html = u'<select name="'+name+'" id="'+name+u'"'+u">\n"
    
    keys = roles.keys()
    keys.sort()
    
    for key in keys:
        html += u'<option value="'+key+u'"'
        if selected != '' and selected == key:
            html += u' selected="selected"'
        html += u'>'+roles[key]+u"</option>\n"
        
    html += u"</select>\n"
    
    return html
    
