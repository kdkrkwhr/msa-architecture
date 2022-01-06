package com.kdk.filter;

import javax.servlet.http.HttpServletRequest;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import com.netflix.zuul.ZuulFilter;
import com.netflix.zuul.context.RequestContext;

public class PreFilter extends ZuulFilter {

  private static final Logger logger = LoggerFactory.getLogger(PreFilter.class);

  @Override
  public String filterType() {
    return "pre";
  }

  @Override
  public int filterOrder() {
    return 0;
  }

  @Override
  public boolean shouldFilter() {
    return true;
  }

  @Override
  public Object run() {
    RequestContext requestContext = RequestContext.getCurrentContext();
    HttpServletRequest httpServletRequest = requestContext.getRequest();
    logger.info("===== ZUUL::PRE =====");
    logger.info("Request URL :: {} Request Method :: {}", 
        httpServletRequest.getRequestURI(),
        httpServletRequest.getMethod());

    return null;
  }
}
