/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.Productos.CRUD_PRODUCTOS.controller;

import com.Productos.CRUD_PRODUCTOS.model.Producto;
import com.Productos.CRUD_PRODUCTOS.service.ProductoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

/**
 *
 * @author Yisus
 */
@Controller
@RequestMapping("/productos")
public class ProductoController {
  
    @Autowired
    private ProductoService productoService;
  
    @GetMapping
    public String listarProductos(Model model) {
        model.addAttribute("productos", productoService.listarTodas());
        return "producto-list";
    }
  
    @GetMapping("/nuevo")
    public String mostrarFormularioNuevoProducto(Model model) {
        model.addAttribute("producto", new Producto());
        return "producto-form";
    }
  
    @PostMapping
    public String guardarProducto(Producto producto) {
        productoService.guardar(producto);
        return "redirect:/productos";
    }
  
    @GetMapping("/editar/{id}")
    public String mostrarFormularioEditarProducto(@PathVariable Long id, Model model) {
        model.addAttribute("producto", productoService.obtenerPorId(id));
        return "producto-form";
    }
  
    @GetMapping("/eliminar/{id}")
    public String eliminarProducto(@PathVariable Long id) {
        productoService.eliminar(id);
        return "redirect:/productos";
    }
}