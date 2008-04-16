<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    <xsl:output omit-xml-declaration="yes"/>
    <xsl:param name="pid">changemeplease</xsl:param>
    <!-- To convert things to lowercase: -->
    <xsl:variable name="lcletters">abcdefghijklmnopqrstuvwxyz</xsl:variable>
    <xsl:variable name="ucletters">ABCDEFGHIJKLMNOPQRSTUVWXYZ</xsl:variable>
    <xsl:template match="mods:mods" xmlns:mods="http://www.loc.gov/mods/v3">
        <!--                 Add all names to the name sections for this index record.
                        Good idea? Maybe, worth a go anyway 
                        Adding individual terms:
-->
        <xsl:choose>
            <xsl:when test="//mods:identifier[@type='pid']">
                <xsl:element name="field">
                    <xsl:attribute name="name">id</xsl:attribute>
                    <xsl:value-of select="//mods:identifier[@type='pid']"/>
                </xsl:element>
            </xsl:when>
            <xsl:when test="not($pid='changemeplease')">
                <xsl:element name="field">
                    <xsl:attribute name="name">id</xsl:attribute>
                    <xsl:value-of select="$pid"/>
                </xsl:element>
            </xsl:when>
        </xsl:choose>

        <xsl:for-each select="//mods:namePart">
            <xsl:call-template name="name"/>
        </xsl:for-each>
        <!--                Now adding complete names and handling affiliations
-->
        <xsl:for-each select="//mods:name">
            <xsl:call-template name="namesection"/>
        </xsl:for-each>
        <xsl:for-each select="mods:titleInfo">
            <xsl:call-template name="titleInfo"/>
        </xsl:for-each>
        <xsl:for-each select="mods:subject">
            <xsl:call-template name="subject"/>
        </xsl:for-each>
        <xsl:for-each select="mods:genre">
            <xsl:call-template name="genre"/>
        </xsl:for-each>
        <xsl:for-each select="mods:typeOfResource">
            <xsl:call-template name="typeofresource"/>
        </xsl:for-each>
        <xsl:for-each select="mods:abstract">
            <xsl:call-template name="abstract"/>
        </xsl:for-each>
        <xsl:for-each select="mods:description">
            <xsl:call-template name="description"/>
        </xsl:for-each>
        <xsl:for-each select="mods:identifier">
            <xsl:call-template name="identifier"/>
        </xsl:for-each>
        <xsl:for-each select="mods:originInfo">
            <xsl:call-template name="origininfo"/>
        </xsl:for-each>
        <xsl:for-each select="mods:extension/etd:degree" xmlns:etd="http://www.ouls.ox.ac.uk/ora/modsextensions">
            <xsl:call-template name="ethesis"></xsl:call-template>
        </xsl:for-each>
        <xsl:for-each select="mods:relatedItem">
            <xsl:call-template name="relateditem"/>
        </xsl:for-each>
        <xsl:for-each select="mods:physicalDescription">
            <xsl:call-template name="physicaldescription"/>
        </xsl:for-each>
        <!--                Now to add the simpler fields:       -->
        <xsl:for-each select="mods:language/mods:languageTerm">
            <xsl:element name="field">
                <xsl:attribute name="name">language</xsl:attribute>
                <xsl:value-of select="normalize-space(.)"/>
            </xsl:element>
        </xsl:for-each>
    </xsl:template>
    <xsl:template name="titleInfo" xmlns:mods="http://www.loc.gov/mods/v3">
        <xsl:for-each select="mods:title">
            <xsl:element name="field">
                <xsl:attribute name="name">title</xsl:attribute>
                <xsl:value-of select="normalize-space(.)"/>
            </xsl:element>
        </xsl:for-each>
        <xsl:for-each select="mods:subTitle">
            <xsl:element name="field">
                <xsl:attribute name="name">subtitle</xsl:attribute>
                <xsl:value-of select="normalize-space(.)"/>
            </xsl:element>
        </xsl:for-each>
    </xsl:template>
    <xsl:template name="name" xmlns:mods="http://www.loc.gov/mods/v3">
        <xsl:choose>
            <xsl:when test="count(@type)=1">
                <xsl:if test="not(@type='termsOfAddress')">
                    <xsl:element name="field">
                        <xsl:attribute name="name">
                            <xsl:value-of select="@type"/>
                        </xsl:attribute>
                        <xsl:value-of select="normalize-space(.)"/>
                    </xsl:element>
                </xsl:if>
            </xsl:when>
        </xsl:choose>
    </xsl:template>
    <xsl:template name="subject" xmlns:mods="http://www.loc.gov/mods/v3">
        <xsl:for-each select="mods:genre">
            <xsl:element name="field">
                <xsl:attribute name="name">keyphrase</xsl:attribute>
                <xsl:value-of select="normalize-space(.)"/>
            </xsl:element>
        </xsl:for-each>
        <xsl:for-each select="mods:topic">
            <xsl:element name="field">
                <xsl:attribute name="name">subject</xsl:attribute>
                <xsl:value-of select="normalize-space(.)"/>
            </xsl:element>
        </xsl:for-each>
    </xsl:template>
    <xsl:template name="typeofresource" xmlns:mods="http://www.loc.gov/mods/v3">
        <xsl:element name="field">
            <xsl:attribute name="name">typeofresource</xsl:attribute>
            <xsl:value-of select="normalize-space(.)"/>
        </xsl:element>
    </xsl:template>
    <xsl:template name="abstract" xmlns:mods="http://www.loc.gov/mods/v3">
        <xsl:element name="field">
            <xsl:attribute name="name">abstract</xsl:attribute>
            <xsl:value-of select="normalize-space(.)"/>
        </xsl:element>
    </xsl:template>
    <xsl:template name="description" xmlns:mods="http://www.loc.gov/mods/v3">
        <xsl:element name="field">
            <xsl:attribute name="name">description</xsl:attribute>
            <xsl:value-of select="normalize-space(.)"/>
        </xsl:element>
    </xsl:template>
    <xsl:template name="namesection" xmlns:mods="http://www.loc.gov/mods/v3">
        <xsl:if test="mods:namePart[@type='family']">
            <xsl:choose>
                <xsl:when test="translate(mods:role/mods:roleTerm,$ucletters,$lcletters) = 'copyright_holder'"></xsl:when>
                <xsl:when test="translate(mods:role/mods:roleTerm,$ucletters,$lcletters) = 'publisher'"></xsl:when>
                <xsl:when test="translate(mods:role/mods:roleTerm,$ucletters,$lcletters) = 'supervisor'"></xsl:when>
                <xsl:when test="translate(mods:role/mods:roleTerm,$ucletters,$lcletters) = 'author'"></xsl:when>
                <xsl:otherwise>
                    <xsl:element name="field">
                        <xsl:attribute name="name">person_name</xsl:attribute>
                        <xsl:value-of select="./mods:namePart[@type='given']"/>
                        <xsl:text> </xsl:text>
                        <xsl:value-of select="./mods:namePart[@type='family']"/>
                    </xsl:element>
                </xsl:otherwise>
               </xsl:choose>
            <xsl:element name="field">
                <xsl:attribute name="name">fullname</xsl:attribute>
                <xsl:value-of select="./mods:namePart[@type='given']"/>
                <xsl:text> </xsl:text>
                <xsl:value-of select="./mods:namePart[@type='family']"/>
            </xsl:element>
        </xsl:if>
        <xsl:if test="mods:displayForm">
            <xsl:element name="field">
                <xsl:attribute name="name">fullname</xsl:attribute>
                <xsl:value-of select="./mods:displayForm"/>
            </xsl:element>
        </xsl:if>
        <xsl:choose>
            <xsl:when test="translate(mods:role/mods:roleTerm,$ucletters,$lcletters) = 'author'">
                <xsl:if test="mods:displayForm">
                    <xsl:element name="field">
                        <xsl:attribute name="name">author</xsl:attribute>
                        <xsl:value-of select="mods:displayForm"/>
                    </xsl:element>
                </xsl:if>
                <xsl:if test="mods:namePart[@type='family']">
                    <xsl:element name="field">
                        <xsl:attribute name="name">author</xsl:attribute>
                        <xsl:value-of select="./mods:namePart[@type='given']"/>
                        <xsl:text> </xsl:text>
                        <xsl:value-of select="./mods:namePart[@type='family']"/>
                    </xsl:element>
                </xsl:if>
                <xsl:choose>
                    <xsl:when test="mods:displayForm">
                        <xsl:element name="field">
                            <xsl:attribute name="name">person_name</xsl:attribute>
                            <xsl:value-of select="mods:displayForm"/>
                        </xsl:element>
                    </xsl:when>
                    <xsl:otherwise>
                        <xsl:if test="mods:namePart[@type='family']">
                            <xsl:element name="field">
                                <xsl:attribute name="name">person_name</xsl:attribute>
                                <xsl:value-of select="./mods:namePart[@type='family']"/>
                                <xsl:text>, </xsl:text>
                                <xsl:value-of select="./mods:namePart[@type='given']"/>
                            </xsl:element>
                        </xsl:if>
                        <xsl:if test="count(mods:namePart[@type])=0">
                            <xsl:element name="field">
                                <xsl:attribute name="name">person_name</xsl:attribute>
                                <xsl:value-of select="mods:namePart"/>
                            </xsl:element>
                        </xsl:if>
                    </xsl:otherwise>
                </xsl:choose>
                <!--
                    <xsl:if test="mods:displayForm">
                        <xsl:element name="field">
                            <xsl:attribute name="name">person_name</xsl:attribute>
                            <xsl:value-of select="mods:displayForm"/>
                        </xsl:element>
                    </xsl:if> -->
                    
            </xsl:when>
            <xsl:when test="translate(mods:role/mods:roleTerm,$ucletters,$lcletters) = 'funder'">
                <xsl:if test="mods:displayForm">
                    <xsl:element name="field">
                        <xsl:attribute name="name">funder</xsl:attribute>
                        <xsl:value-of select="mods:displayForm"/>
                    </xsl:element>
                </xsl:if>
                <xsl:if test="mods:namePart[@type='family']">
                    <xsl:element name="field">
                        <xsl:attribute name="name">funder</xsl:attribute>
                        <xsl:value-of select="./mods:namePart[@type='given']"/>
                        <xsl:text> </xsl:text>
                        <xsl:value-of select="./mods:namePart[@type='family']"/>
                    </xsl:element>
                </xsl:if>
            </xsl:when>
            <xsl:when test="translate(mods:role/mods:roleTerm,$ucletters,$lcletters) = 'supervisor'">
                <xsl:if test="mods:displayForm">
                    <xsl:element name="field">
                        <xsl:attribute name="name">supervisor</xsl:attribute>
                        <xsl:value-of select="mods:displayForm"/>
                    </xsl:element>
                </xsl:if>
                <xsl:if test="mods:namePart[@type='family']">
                    <xsl:element name="field">
                        <xsl:attribute name="name">supervisor</xsl:attribute>
                        <xsl:value-of select="./mods:namePart[@type='given']"/>
                        <xsl:text> </xsl:text>
                        <xsl:value-of select="./mods:namePart[@type='family']"/>
                    </xsl:element>
                </xsl:if>
            </xsl:when>
            <xsl:when test="translate(mods:role/mods:roleTerm,$ucletters,$lcletters) = 'editor'">
                <xsl:if test="mods:displayForm">
                    <xsl:element name="field">
                        <xsl:attribute name="name">editor</xsl:attribute>
                        <xsl:value-of select="mods:displayForm"/>
                    </xsl:element>
                </xsl:if>
                <xsl:if test="mods:namePart[@type='family']">
                    <xsl:element name="field">
                        <xsl:attribute name="name">editor</xsl:attribute>
                        <xsl:value-of select="./mods:namePart[@type='given']"/>
                        <xsl:text> </xsl:text>
                        <xsl:value-of select="./mods:namePart[@type='family']"/>
                    </xsl:element>
                </xsl:if>
                <xsl:if test="count(mods:namePart[@type])=0">
                    <xsl:element name="field">
                        <xsl:attribute name="name">person_name</xsl:attribute>
                        <xsl:value-of select="mods:namePart"/>
                    </xsl:element>
                </xsl:if>
            </xsl:when>
            <xsl:when test="translate(mods:role/mods:roleTerm,$ucletters,$lcletters) = 'principal investigator'">
                <xsl:if test="mods:displayForm">
                    <xsl:element name="field">
                        <xsl:attribute name="name">principal_investigator</xsl:attribute>
                        <xsl:value-of select="mods:displayForm"/>
                    </xsl:element>
                </xsl:if>
                <xsl:if test="mods:namePart[@type='family']">
                    <xsl:element name="field">
                        <xsl:attribute name="name">principal_investigator</xsl:attribute>
                        <xsl:value-of select="./mods:namePart[@type='given']"/>
                        <xsl:text> </xsl:text>
                        <xsl:value-of select="./mods:namePart[@type='family']"/>
                    </xsl:element>
                </xsl:if>
                <xsl:if test="count(mods:namePart[@type])=0">
                    <xsl:element name="field">
                        <xsl:attribute name="name">person_name</xsl:attribute>
                        <xsl:value-of select="mods:namePart"/>
                    </xsl:element>
                </xsl:if>
            </xsl:when>
            <xsl:when test="translate(mods:role/mods:roleTerm,$ucletters,$lcletters) = 'publisher'">
                <xsl:if test="mods:displayForm">
                    <xsl:element name="field">
                        <xsl:attribute name="name">publisher</xsl:attribute>
                        <xsl:value-of select="mods:displayForm"/>
                    </xsl:element>
                </xsl:if>
                <xsl:if test="mods:namePart[@type='family']">
                    <xsl:element name="field">
                        <xsl:attribute name="name">publisher</xsl:attribute>
                        <xsl:value-of select="./mods:namePart[@type='given']"/>
                        <xsl:text> </xsl:text>
                        <xsl:value-of select="./mods:namePart[@type='family']"/>
                    </xsl:element>
                </xsl:if>
            </xsl:when>
            <xsl:when test="translate(mods:role/mods:roleTerm,$ucletters,$lcletters) = 'copyright holder'">
                <xsl:if test="mods:displayForm">
                    <xsl:element name="field">
                        <xsl:attribute name="name">copyright_holder</xsl:attribute>
                        <xsl:value-of select="mods:displayForm"/>
                    </xsl:element>
                </xsl:if>
                <xsl:if test="mods:namePart[@type='family']">
                    <xsl:element name="field">
                        <xsl:attribute name="name">copyright_holder</xsl:attribute>
                        <xsl:value-of select="./mods:namePart[@type='given']"/>
                        <xsl:text> </xsl:text>
                        <xsl:value-of select="./mods:namePart[@type='family']"/>
                    </xsl:element>
                </xsl:if>
            </xsl:when>
        </xsl:choose>

        <xsl:if test="count(mods:namePart)=1">
            <xsl:element name="field">
                <xsl:attribute name="name">fullname</xsl:attribute>
                <xsl:value-of select="mods:namePart"/>
            </xsl:element>
        </xsl:if>
        <xsl:for-each select="./mods:affiliation">
            <xsl:if test="not(@type='email')">
                <xsl:element name="field">
                    <xsl:attribute name="name">
                        <xsl:value-of select="@type"/>
                    </xsl:attribute>
                    <xsl:value-of select="normalize-space(.)"/>
                </xsl:element>
            </xsl:if>
        </xsl:for-each>
    </xsl:template>
    <xsl:template name="genre" xmlns:mods="http://www.loc.gov/mods/v3">
        <xsl:element name="field">
            <xsl:attribute name="name">genre</xsl:attribute>
            <xsl:value-of select="normalize-space(.)"/>
        </xsl:element>
    </xsl:template>
    <xsl:template name="identifier" xmlns:mods="http://www.loc.gov/mods/v3">
        <xsl:choose>
            <xsl:when test="@type='additional'"/>
            <xsl:when test="@type='uri'">
                <xsl:element name="field">
                    <xsl:attribute name="name">identifier</xsl:attribute>
                    <xsl:value-of select="normalize-space(.)"/>
                </xsl:element>
            </xsl:when>
            <xsl:when test="@type='conference-site'">
                <xsl:element name="field">
                    <xsl:attribute name="name">website</xsl:attribute>
                    <xsl:value-of select="normalize-space(.)"/>
                </xsl:element>
            </xsl:when>
            <xsl:when test="@type">
                <xsl:element name="field">
                    <xsl:attribute name="name">
                        <xsl:value-of select="@type"/>
                    </xsl:attribute>
                    <xsl:value-of select="normalize-space(.)"/>
                </xsl:element>
            </xsl:when>
            <xsl:otherwise>
                <xsl:element name="field">
                    <xsl:attribute name="name">identifier</xsl:attribute>
                    <xsl:value-of select="normalize-space(.)"/>
                </xsl:element>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>
    <xsl:template name="origininfo" xmlns:mods="http://www.loc.gov/mods/v3">
        <xsl:if test="mods:edition">
            <xsl:element name="field">
                <xsl:attribute name="name">edition</xsl:attribute>
                <xsl:value-of select="mods:edition"/>
            </xsl:element>
        </xsl:if>
        <xsl:if test="mods:dateIssued">
            <xsl:element name="field">
                <xsl:attribute name="name">issue_date</xsl:attribute>
                <xsl:value-of select="mods:dateIssued"/>
            </xsl:element>
        </xsl:if>
        <xsl:if test="mods:dateCreated">
            <xsl:element name="field">
                <xsl:attribute name="name">creation_date</xsl:attribute>
                <xsl:value-of select="mods:dateCreated"/>
            </xsl:element>
        </xsl:if>
        <xsl:if test="mods:dateModified">
            <xsl:element name="field">
                <xsl:attribute name="name">modified_date</xsl:attribute>
                <xsl:value-of select="mods:dateModified"/>
            </xsl:element>
        </xsl:if>
        <xsl:if test="mods:copyrightDate">
            <xsl:element name="field">
                <xsl:attribute name="name">copyright_date</xsl:attribute>
                <xsl:value-of select="mods:copyrightDate"/>
            </xsl:element>
        </xsl:if>
        <xsl:if test="mods:publisher">
            <xsl:element name="field">
                <xsl:attribute name="name">publisher</xsl:attribute>
                <xsl:value-of select="mods:publisher"/>
            </xsl:element>
        </xsl:if>
        <xsl:if test="mods:place">
            <xsl:element name="field">
                <xsl:attribute name="name">place</xsl:attribute>
                <xsl:value-of select="mods:place"/>
            </xsl:element>
        </xsl:if>
    </xsl:template>
    <xsl:template name="physicaldescription" xmlns:mods="http://www.loc.gov/mods/v3">
        <xsl:for-each select="mods:form">
            <xsl:choose>
                <xsl:when test="@type='peerReviewed'">
                    <xsl:if test="translate(text(),$ucletters,$lcletters)='peer reviewed'">
                        <xsl:element name="field">
                            <xsl:attribute name="name"
                        >peer_reviewed</xsl:attribute>True</xsl:element>
                    </xsl:if>
                    <xsl:element name="field">
                        <xsl:attribute name="name">review_status</xsl:attribute>
                        <xsl:value-of select="normalize-space(.)"/>
                    </xsl:element>
                </xsl:when>
                <xsl:when test="translate(@type,$ucletters,$lcletters)='status'">
                    <xsl:element name="field">
                        <xsl:attribute name="name">status</xsl:attribute>
                        <xsl:value-of select="normalize-space(.)"/>
                    </xsl:element>
                </xsl:when>
                <xsl:when test="translate(@type,$ucletters,$lcletters)='version'">
                    <xsl:element name="field">
                        <xsl:attribute name="name">version</xsl:attribute>
                        <xsl:value-of select="normalize-space(.)"/>
                    </xsl:element>
                </xsl:when>
            </xsl:choose>
        </xsl:for-each>
    </xsl:template>
    <xsl:template name="relateditem" xmlns:mods="http://www.loc.gov/mods/v3">
        <xsl:choose>
            <xsl:when test="@type='host'">
                <xsl:for-each select="mods:titleInfo/mods:title">
                    <xsl:element name="field">
                        <xsl:attribute name="name">host</xsl:attribute>
                        <xsl:value-of select="normalize-space(.)"/>
                    </xsl:element>
                </xsl:for-each>
                <xsl:for-each select="mods:part">
                    <xsl:for-each select="mods:detail">
                        <xsl:if test="translate(@type,$ucletters,$lcletters)='volume'">
                            <xsl:element name="field">
                                <xsl:attribute name="name">volume</xsl:attribute>
                                <xsl:value-of select="mods:number"/>
                            </xsl:element>
                        </xsl:if>
                        <xsl:if test="translate(@type,$ucletters,$lcletters)='issue'">
                            <xsl:element name="field">
                                <xsl:attribute name="name">issue</xsl:attribute>
                                <xsl:value-of select="mods:number"/>
                            </xsl:element>
                        </xsl:if>
                    </xsl:for-each>
                    <xsl:for-each select="mods:extent">
                        <xsl:if test="translate(@unit,$ucletters,$lcletters)='pages'">
                            <xsl:element name="field">
                                <xsl:attribute name="name">pages</xsl:attribute>
                                <xsl:value-of select="mods:list"/>
                            </xsl:element>
                        </xsl:if>
                    </xsl:for-each>
                </xsl:for-each>
            </xsl:when>            
        </xsl:choose>            
    </xsl:template>
    <xsl:template name="ethesis"  xmlns:etd="http://www.ouls.ox.ac.uk/ora/modsextensions">
        <xsl:if test="count(etd:name)=1">
            <xsl:element name="field">
                <xsl:attribute name="name">thesis_type</xsl:attribute>
                <xsl:value-of select="etd:name"/>
            </xsl:element>
        </xsl:if>
        <xsl:if test="count(etd:level)=1">
            <xsl:element name="field">
                <xsl:attribute name="name">thesis_level</xsl:attribute>
                <xsl:value-of select="etd:level"/>
            </xsl:element>
        </xsl:if>
    </xsl:template>
</xsl:stylesheet>
