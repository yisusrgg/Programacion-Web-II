/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.Productos.CRUD_PRODUCTOS.service;

import com.Productos.CRUD_PRODUCTOS.model.Producto;
import com.Productos.CRUD_PRODUCTOS.repository.ProductoRepository;
import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

/**
 *
 * @author Yisus
 */
@Service
public class ProductoService {
    @Autowired
        private ProductoRepository productoRepository;
      
        public List<Producto> listarTodas() {
            return productoRepository.findAll();
        }
      
        public void guardar(Producto producto) {
            if (producto.getIdProducto() != null) {
                productoRepository.save(producto); // JPA detecta ID y hace UPDATE
            } else {
                productoRepository.save(producto); // JPA detecta null y hace INSERT
            }
        }
      
        public Producto obtenerPorId(Long id) {
            return productoRepository.findById(id).orElse(null);
        }
      
        public void eliminar(Long id) {
            productoRepository.deleteById(id);
        }
    

}
