package com.delivery.restaurantes.repository;

import com.delivery.restaurantes.entity.Restaurante;
import org.springframework.data.jpa.repository.JpaRepository;

public interface RestauranteRepository extends JpaRepository<Restaurante, Long> {
    
}
