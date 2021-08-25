package com.kdk;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.cloud.client.loadbalancer.LoadBalanced;
import org.springframework.context.annotation.Bean;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

@EnableDiscoveryClient
@SpringBootApplication
public class DefaultServerApplication {

  public static void main(String[] args) {
    SpringApplication.run(DefaultServerApplication.class, args);
  }

  @Bean
  @LoadBalanced
  public RestTemplate restTemplate() {
    return new RestTemplate();
  }

  @RestController
  class EurekaClientController {

    @Autowired
    RestTemplate restTemplate;

    @GetMapping("/eureka/client")
    public String eurekaClient() {
      String result = restTemplate.getForObject("http://eurekaclient/eureka/client", String.class);
      return result;
    }
  }
}
