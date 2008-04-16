<?xml version="1.0" encoding="UTF-8"?>
 <OpenSearchDescription xmlns="http://a9.com/-/spec/opensearch/1.1/" xmlns:moz="http://www.mozilla.org/2006/browser/search/">
   <ShortName>ORA Search</ShortName>
   <Description>Search inside the content of the Oxford University Research Archive.</Description>
   <Url type="application/atom+xml"
        template="${g.root}${h.url_for(controller='search', action='detailed')}?q={searchTerms}&amp;view=Default&amp;start={startIndex?}&amp;format=atom"/>
   <Url type="text/html" 
        template="${g.root}${h.url_for(controller='search', action='detailed')}?q={searchTerms}&amp;start={startIndex?}"/>
   <Image height="16" width="16" type="image/x-icon">http://archive.sers.ox.ac.uk:5000/favicon.ico</Image>
   <Tags>example web</Tags>
   <Contact>admin@example.com</Contact>
   <AdultContent>false</AdultContent>
   <Language>en-gb</Language>
   <OutputEncoding>UTF-8</OutputEncoding>
   <InputEncoding>UTF-8</InputEncoding>
   <moz:SearchForm>${g.root}${h.url_for(controller='search', action='detailed')}</moz:SearchForm>
   <moz:UpdateUrl>${g.root}${h.url_for(controller='search', action='opensearch')}</moz:UpdateUrl>
   <moz:UpdateInterval>7</moz:UpdateInterval>
 </OpenSearchDescription>
