package com.delivery.pedidos.controller;

import com.delivery.pedidos.entity.Pedido;
import com.delivery.pedidos.service.PedidoService;
import java.util.List;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.HttpStatus;
import org.springframework.web.server.ResponseStatusException;

@RestController
@RequestMapping("/pedidos")
public class PedidoController {

    private final PedidoService service;

    public PedidoController(PedidoService service) {
        this.service = service;
    }

    @PostMapping
    public Pedido cadastrar(@RequestBody Pedido pedido) {
        try {
            return service.salvar(pedido);
        } catch (IllegalArgumentException e) {
            throw new ResponseStatusException(
                    HttpStatus.BAD_REQUEST, e.getMessage()
            );
        }
    }

    @GetMapping
    public List<Pedido> listarTodos() {
        return service.listarTodos();
    }

    @GetMapping("/{id}")
    public Pedido buscarPorId(@PathVariable Long id) {
        Pedido pedido = service.buscarPorId(id);

        if (pedido == null) {
            throw new ResponseStatusException(
                    HttpStatus.NOT_FOUND, "Pedido não encontrado!"
            );
        }

        return pedido;
    }

    @DeleteMapping("/{id}")
    public void excluir(@PathVariable Long id) {
        service.excluir(id);
    }
}