<?php # -*- coding: utf-8 -*-
/*
 * Plugin Name: Odoo Menu
 * Version:	0.1.0
 * */

add_shortcode( 'odoomenu', 'show_odoomenu' );

function show_odoomenu( $attributes )
{
    $pluginDir = '/wp-content/plugins/odoomenu/';
    $odooMenuUri = 'https://odoomenu.codefounders.nl';

    $handle = 'odoocss';
    wp_register_style( $handle, $odooMenuUri.$pluginDir.'web.assets_common.css', array(), '', 'all' );
    wp_enqueue_style( $handle, 'wp-contentAA' );

    $handle1 = 'odoocss1';
    wp_register_style( $handle1, $odooMenuUri.$pluginDir.'web.assets_frontend.css', array(), '', 'all' );
    wp_enqueue_style( $handle1 );

    $handle3 = 'odoocss3';
    wp_register_style( $handle3, $odooMenuUri.$pluginDir.'odoomenu-plugin.css', array(), '', 'all' );
    wp_enqueue_style( $handle3 );

    $handle2 = 'odoocss2';
    wp_register_script( $handle2, $odooMenuUri.$pluginDir.'web.assets_common_lazy.js', array(), '', true );
    wp_enqueue_script( $handle2 );

    $handle4 = 'odoocss4';
    wp_register_script( $handle4, $odooMenuUri.$pluginDir.'odoomenu.js', array(), '', true );
    wp_enqueue_script( $handle4 );

    $response = wp_remote_get( $odooMenuUri.$pluginDir.'/odoomenu-minimal.html' );
    $body     = wp_remote_retrieve_body( $response );

    return $body;
}
