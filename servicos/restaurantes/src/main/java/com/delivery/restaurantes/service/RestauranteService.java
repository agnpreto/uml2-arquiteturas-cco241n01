package com.delivery.restaurantes.service;

import com.delivery.restaurantes.entity.Restaurante;
import com.delivery.restaurantes.repository.RestauranteRepository;
import java.util.List;
import java.util.Optional;
import org.springframework.stereotype.Service;

@Service
public class RestauranteService {

    private final RestauranteRepository restauranteRepository;

    public RestauranteService(RestauranteRepository restauranteRepository) {
        this.restauranteRepository = restauranteRepository;
    }

    public Restaurante cadastrar(Restaurante restaurante) {
        return restauranteRepository.save(restaurante);
    }

    public List<Restaurante> listarTodos() {
        return restauranteRepository.findAll();
    }

    public Optional<Restaurante> buscarPorId(Long id) {
        return restauranteRepository.findById(id);
    }

    public Restaurante atualizar(Long id, Restaurante restauranteAtualizado) {
        return restauranteRepository.findById(id)
                .map(restaurante -> {
                    restaurante.setNome(restauranteAtualizado.getNome());
                    restaurante.setEndereco(restauranteAtualizado.getEndereco());
                    restaurante.setTelefone(restauranteAtualizado.getTelefone());
                    restaurante.setAtivo(restauranteAtualizado.isAtivo());

                    return restauranteRepository.save(restaurante);
                })
                .orElseThrow(() -> new RuntimeException("Restaurante não encontrado!"));
    }

    public void excluir(Long id) {
        restauranteRepository.deleteById(id);
    }

    
}
