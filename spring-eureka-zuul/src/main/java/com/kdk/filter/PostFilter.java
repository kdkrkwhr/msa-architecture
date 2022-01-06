package com.kdk.filter;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import com.netflix.zuul.ZuulFilter;

public class PostFilter extends ZuulFilter {

  private static final Logger logger = LoggerFactory.getLogger(RouteFilter.class);

  @Override
  public String filterType() {
    return "POST";
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
    logger.info("===== ZUUL::POST =====");
    return null;
  }
}
