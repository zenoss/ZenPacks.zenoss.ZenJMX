/*****************************************************************************
 * 
 * Copyright (C) Zenoss, Inc. 2016, all rights reserved.
 * 
 * This content is made available according to terms specified in
 * License.zenoss under the directory where your Zenoss product is installed.
 * 
 ****************************************************************************/


package com.zenoss.zenpacks.zenjmx;

import org.apache.xmlrpc.webserver.XmlRpcServlet;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class ZenXmlRpcServlet extends XmlRpcServlet {

    @Override
    protected void doTrace(HttpServletRequest req, HttpServletResponse resp) { 
        resp.setStatus(HttpServletResponse.SC_METHOD_NOT_ALLOWED); 
    }
}
