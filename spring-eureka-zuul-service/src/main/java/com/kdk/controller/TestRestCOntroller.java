package com.kdk.controller;

import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping(value = "/api", produces = MediaType.APPLICATION_JSON_VALUE)
public class TestRestCOntroller {

  @RequestMapping(value = "/{value}", method = RequestMethod.GET)
  public String eurekaClient(@PathVariable("value") String value) {
    return value == null ? "NA" : value;
  }
}
