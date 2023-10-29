% Hechos videojuegos
videojuego(the_witcher_3).
videojuego(minecraft).
videojuego(gta_v).
videojuego(overwatch_2).
videojuego(zelda_botw).
videojuego(valorant).
videojuego(pubg).
videojuego(genshin_impact).
videojuego(world_of_warships).
videojuego(world_of_tanks).
videojuego(smite).
videojuego(lol).
videojuego(skyrim).
videojuego(the_elder_scrolls).
videojuego(assasin_creed).
videojuego(payday_2).
videojuego(payday_3).
videojuego(no_man_sky).
videojuego(cs:go).
videojuego(rocket_league).
videojuego(insurgency_sandstorm).
videojuego(ready_or_not).
videojuego(team_fortress_2).
videojuego(rainbow_six_siege).
videojuego(arma_3).
videojuego(fifa_2023).
videojuego(fallout_4).
videojuego(killing_floor_2).
videojuego(left_4_dead_2).
videojuego(mortal_kombat_11).
videojuego(project_zomboid).
videojuego(spec_ops_the_line).
videojuego(limbo).
videojuego(war_thunder).
videojuego(cup_head).
videojuego(hollow_knight).
videojuego(unturned).
videojuego(sniper_elite_4).
videojuego(ace_combat_7).
videojuego(project_wingman).
videojuego(red_dead_redemption_2).
videojuego(metal_gear_rising).
videojuego(battlefield_4).
videojuego(dying_light).


% Hechos precio
precio(the_witcher_3, 25).
precio(minecraft, 60).
precio(gta_v, 50).
precio(overwatch, 0).
precio(zelda_botw, 45).
precio(valorant,0).
precio(pubg,0).
precio(genshin_impact,0).
precio(world_of_warships,0).
precio(world_of_tanks,0).
precio(smite,0).
precio(lol,0).
precio(skyrim,30).
precio(the_elder_scrolls,0).
precio(assasin_creed,30).
precio(payday_2,10).
precio(payday_3,50).
precio(no_man_sky,30).
precio(cs:go,0).
precio(rocket_league,0).
precio(insurgency_sandstorm,30).
precio(ready_or_not,30).
precio(team_fortress_2,0).
precio(rainbow_six_siege,30).
precio(arma_3,30).
precio(fifa_2023,60).
precio(fallout_4,10).
precio(killing_floor_2,30).
precio(left_4_dead_2,5).
precio(mortal_kombat_11,60).
precio(project_zomboid,15).
precio(spec_ops_the_line,10).
precio(limbo,7).
precio(war_thunder,0).
precio(cup_head,10).
precio(hollow_knight,10).
precio(unturned,0).
precio(sniper_elite_4,30).
precio(ace_combat_7,60).
precio(project_wingman,30).
precio(red_dead_redemption_2,60).
precio(metal_gear_rising,30).
precio(battlefield_4,30).
precio(dying_light,15).

% Hechos categoria
categoria(the_witcher_3, rpg).
categoria(minecraft, sandbox).
categoria(gta_v, accion).
categoria(overwatch, shooter).
categoria(zelda_botw, aventura).
categoria(valorant,shooter).
categoria(pubg,shooter).
categoria(genshin_impact,aventura).
categoria(world_of_warships,vehiculos).
categoria(world_of_tanks,vehiculos).
categoria(smite,mmo).
categoria(lol,mmo).
categoria(skyrim,rpg).
categoria(the_elder_scrolls,rpg).
categoria(assasin_creed,accion).
categoria(payday_2,shooter).
categoria(payday_3,shooter).
categoria(no_man_sky,aventura).
categoria(cs:go,shooter).
categoria(rocket_league,deportes).
categoria(insurgency_sandstorm,shooter).
categoria(ready_or_not,shooter).
categoria(team_fortress_2,accion).
categoria(rainbow_six_siege,shooter).
categoria(arma_3,shooter).
categoria(fifa_2023,deportes).
categoria(fallout_4,sandbox).
categoria(killing_floor_2,accion).
categoria(left_4_dead_2,accion).
categoria(mortal_kombat_11,accion).
categoria(project_zomboid,sandbox).
categoria(spec_ops_the_line,shooter).
categoria(limbo,indie).
categoria(war_thunder,vehiculos).
categoria(cup_head,indie).
categoria(hollow_knight,indie).
categoria(unturned,sandbox).
categoria(sniper_elite_4,shooter).
categoria(ace_combat_7,vehiculos).
categoria(project_wingman,vehiculos).
categoria(red_dead_redemption_2,aventura).
categoria(metal_gear_rising,accion).
categoria(battlefield_4,shooter).
categoria(dying_light,aventura).

% Hechos rating
rating(the_witcher_3, 9.5).
rating(minecraft, 9.0).
rating(gta_v, 8.7).
rating(overwatch, 0.9).
rating(zelda_botw, 9.6).
rating(valorant,8.0).
rating(pubg,8.5).
rating(genshin_impact,9.0).
rating(world_of_warships,6.0).
rating(world_of_tanks,5.0).
rating(smite,7.0).
rating(lol,4.0).
rating(skyrim,7.0).
rating(the_elder_scrolls,7.0).
rating(assasin_creed,7.0).
rating(payday_2,7.5).
rating(payday_3,9.0).
rating(no_man_sky,4.0).
rating(cs:go,9.6).
rating(rocket_league,9.0).
rating(insurgency_sandstorm,9.5).
rating(ready_or_not,10.0).
rating(team_fortress_2,9.3).
rating(rainbow_six_siege,8.2).
rating(arma_3,8.5).
rating(fifa_2023,7.0).
rating(fallout_4,9.3).
rating(killing_floor_2,8.7).
rating(left_4_dead_2,10.0).
rating(mortal_kombat_11,9.0).
rating(project_zomboid,9.5).
rating(spec_ops_the_line,10.0).
rating(limbo,9.0).
rating(war_thunder,9.0).
rating(cup_head,10.0).
rating(hollow_knight,8.0).
rating(unturned,7.0).
rating(sniper_elite_4,7.0).
rating(ace_combat_7,8.8).
rating(project_wingman,9.7).
rating(red_dead_redemption_2,9.4).
rating(metal_gear_rising,9.9).
rating(battlefield_4,10.0).
rating(dying_light,8.8).




videojuegos_por_precio(Precio, Videojuegos) :-
    findall(Videojuego, precio(Videojuego, Precio), Videojuegos).
videojuegos_por_categoria(Categoria, Videojuegos) :-
    findall(Videojuego, categoria(Videojuego, Categoria), Videojuegos).
videojuegos_por_rating(Rating,Videojuegos) :-
    findall(Videojuego, rating(Videojuego, Rating), Videojuegos).


