<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    <xsl:output omit-xml-declaration="yes"/>
    <xsl:param name="content_type">changemeplease</xsl:param>
    <!-- To convert things to lowercase: -->
    <xsl:variable name="lcletters">abcdefghijklmnopqrstuvwxyz</xsl:variable>
    <xsl:variable name="ucletters">ABCDEFGHIJKLMNOPQRSTUVWXYZ</xsl:variable>
    <xsl:template match="rdf:Description" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <xsl:for-each select="rel:isMemberOf"
            xmlns:rel="info:fedora/fedora-system:def/relations-external#">
            <xsl:element name="field">
                <xsl:attribute name="name">content_type</xsl:attribute>
                <xsl:value-of select="substring-after( @rdf:resource, '/type:')"/>
            </xsl:element>
        </xsl:for-each>
        <xsl:for-each select="rel:isMemberOfCollection"
            xmlns:rel="info:fedora/fedora-system:def/relations-external#">
            <xsl:element name="field">
                <xsl:attribute name="name">collection</xsl:attribute>
                <xsl:value-of select="substring-after( @rdf:resource, '/')"/>
            </xsl:element>
        </xsl:for-each>
    </xsl:template>
</xsl:stylesheet>
