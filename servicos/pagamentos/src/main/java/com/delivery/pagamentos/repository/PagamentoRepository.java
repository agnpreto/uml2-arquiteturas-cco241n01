package com.delivery.pagamentos.repository;

import com.delivery.pagamentos.entity.Pagamento;
import org.springframework.data.jpa.repository.JpaRepository;

public interface PagamentoRepository extends JpaRepository<Pagamento, Long> {

}