/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Interface.java to edit this template
 */
package com.Productos.CRUD_PRODUCTOS.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.Productos.CRUD_PRODUCTOS.model.Producto;
import java.util.List;

/**
 *
 * @author Yisus
 */
public interface ProductoRepository extends JpaRepository <Producto, Long> {
    
}
