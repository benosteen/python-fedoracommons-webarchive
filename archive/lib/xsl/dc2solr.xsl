<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    <xsl:output omit-xml-declaration="yes"/>
    <xsl:param name="pid">changemeplease</xsl:param>
    <!-- To convert things to lowercase: -->
    <xsl:variable name="lcletters">abcdefghijklmnopqrstuvwxyz</xsl:variable>
    <xsl:variable name="ucletters">ABCDEFGHIJKLMNOPQRSTUVWXYZ</xsl:variable>
    <xsl:template match="oai_dc:dc" xmlns:oai_dc="http://www.openarchives.org/OAI/2.0/oai_dc/"
        xmlns:dc="http://purl.org/dc/elements/1.1/">
        <xsl:choose>
            <xsl:when test="not($pid='changemeplease')">
                <xsl:element name="field">
                    <xsl:attribute name="name">id</xsl:attribute>
                    <xsl:value-of select="$pid"/>
                </xsl:element>
            </xsl:when>
        </xsl:choose>
        <xsl:for-each select="dc:title">
            <xsl:call-template name="title"/>
        </xsl:for-each>

        <xsl:for-each select="dc:creator">
            <xsl:call-template name="name"/>
        </xsl:for-each>

        <xsl:for-each select="dc:subject">
            <xsl:call-template name="subject"/>
        </xsl:for-each>

        <xsl:for-each select="dc:date">
            <xsl:call-template name="date"/>
        </xsl:for-each>
        <xsl:for-each select="dc:type">
            <xsl:call-template name="type"/>
        </xsl:for-each>
        <xsl:for-each select="dc:format">
            <xsl:call-template name="format"/>
        </xsl:for-each>
        <xsl:for-each select="dc:identifier">
            <xsl:call-template name="identifier"/>
        </xsl:for-each>
        <xsl:for-each select="dc:description">
            <xsl:call-template name="description"/>
        </xsl:for-each>
        <xsl:for-each select="dc:abstract">
            <xsl:call-template name="abstract"/>
        </xsl:for-each>
        <xsl:for-each select="dc:language">
            <xsl:call-template name="language"/>
        </xsl:for-each>
    </xsl:template>
    <xsl:template name="title">
        <xsl:element name="field">
            <xsl:attribute name="name">title</xsl:attribute>
            <xsl:value-of select="normalize-space(.)"/>
        </xsl:element>
    </xsl:template>
    <xsl:template name="name">
        <xsl:variable name="creator_field"><xsl:value-of select="normalize-space(.)"/></xsl:variable>
        <xsl:element name="field">
            <xsl:attribute name="name">fullname</xsl:attribute>
            <xsl:value-of select="$creator_field"/>
        </xsl:element>
        <xsl:element name="field">
            <xsl:attribute name="name">author</xsl:attribute>
            <xsl:value-of select="$creator_field"/>
        </xsl:element>
        <xsl:element name="field">
            <xsl:attribute name="name">person_name</xsl:attribute>
            <xsl:value-of select="$creator_field"/>
        </xsl:element>
    </xsl:template>
    <xsl:template name="subject">
        <xsl:element name="field">
            <xsl:attribute name="name">keyphrase</xsl:attribute>
            <xsl:value-of select="normalize-space(.)"/>
        </xsl:element>
    </xsl:template>
    <xsl:template name="date">
        <xsl:element name="field">
            <xsl:attribute name="name">creation_date</xsl:attribute>
            <xsl:value-of select="normalize-space(.)"/>
        </xsl:element>
    </xsl:template>
    <xsl:template name="type">
        <xsl:element name="field">
            <xsl:attribute name="name">typeofresource</xsl:attribute>
            <xsl:value-of select="normalize-space(.)"/>
        </xsl:element>
    </xsl:template>
    <xsl:template name="format">
        <xsl:element name="field">
            <xsl:attribute name="name">typeofresource</xsl:attribute>
            <xsl:value-of select="normalize-space(.)"/>
        </xsl:element>
        <xsl:element name="field">
            <xsl:attribute name="name">status</xsl:attribute>
            <xsl:value-of select="normalize-space(.)"/>
        </xsl:element>
    </xsl:template>
    <xsl:template name="identifier">
        <xsl:element name="field">
            <xsl:attribute name="name">identifier</xsl:attribute>
            <xsl:value-of select="normalize-space(.)"/>
        </xsl:element>
    </xsl:template>
    <xsl:template name="description">
        <xsl:element name="field">
            <xsl:attribute name="name">description</xsl:attribute>
            <xsl:value-of select="normalize-space(.)"/>
        </xsl:element>
    </xsl:template>
    <xsl:template name="abstract">
        <xsl:element name="field">
            <xsl:attribute name="name">abstract</xsl:attribute>
            <xsl:value-of select="normalize-space(.)"/>
        </xsl:element>
    </xsl:template>
    <xsl:template name="language">
        <xsl:element name="field">
            <xsl:attribute name="name">language</xsl:attribute>
            <xsl:value-of select="normalize-space(.)"/>
        </xsl:element>
    </xsl:template>
</xsl:stylesheet>
