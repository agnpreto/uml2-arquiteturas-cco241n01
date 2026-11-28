package com.delivery.restaurantes.controller;

import com.delivery.restaurantes.entity.Restaurante;
import com.delivery.restaurantes.service.RestauranteService;
import java.util.List;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/restaurantes")
public class RestauranteController {
    
private final RestauranteService restauranteService;

    public RestauranteController(RestauranteService restauranteService) {
        this.restauranteService = restauranteService;
    }

    @PostMapping
    public ResponseEntity<Restaurante> cadastrar(
            @RequestBody Restaurante restaurante) {

        Restaurante novoRestaurante =
                restauranteService.cadastrar(restaurante);

        return ResponseEntity.status(HttpStatus.CREATED)
                .body(novoRestaurante);
    }

    @GetMapping
    public ResponseEntity<List<Restaurante>> listarTodos() {
        return ResponseEntity.ok(
                restauranteService.listarTodos()
        );
    }

    @GetMapping("/{id}")
    public ResponseEntity<Restaurante> buscarPorId(
            @PathVariable Long id) {

        return restauranteService.buscarPorId(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @PutMapping("/{id}")
    public ResponseEntity<Restaurante> atualizar(
            @PathVariable Long id,
            @RequestBody Restaurante restaurante) {

        Restaurante atualizado =
                restauranteService.atualizar(id, restaurante);

        return ResponseEntity.ok(atualizado);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> excluir(@PathVariable Long id) {

        restauranteService.excluir(id);

        return ResponseEntity.noContent().build();
    }
   
}
