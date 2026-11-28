
package com.delivery.pagamentos.service;

import com.delivery.pagamentos.entity.Pagamento;
import com.delivery.pagamentos.repository.PagamentoRepository;
import java.util.List;
import org.springframework.stereotype.Service;
import org.springframework.web.client.HttpClientErrorException;
import org.springframework.web.client.RestClient;

@Service
public class PagamentoService {

    private final PagamentoRepository repository;
    private final RestClient pedidosClient;

    public PagamentoService(PagamentoRepository repository, RestClient.Builder builder) {
        this.repository = repository;

        this.pedidosClient = builder
                .baseUrl("http://localhost:8082")
                .build();
    }

    public Pagamento salvar(Pagamento pagamento) {
        try {
            pedidosClient.get()
                    .uri("/pedidos/{id}", pagamento.getPedidoId())
                    .retrieve()
                    .toBodilessEntity();
        } catch (HttpClientErrorException.NotFound e) {
            throw new IllegalArgumentException("Pedido não encontrado!");
        }

        return repository.save(pagamento);
    }

    public List<Pagamento> listarTodos() {
        return repository.findAll();
    }

    public Pagamento buscarPorId(Long id) {
        return repository.findById(id).orElse(null);
    }

    public void excluir(Long id) {
        repository.deleteById(id);
    }
}
