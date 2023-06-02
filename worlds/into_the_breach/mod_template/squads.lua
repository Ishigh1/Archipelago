return {
    {% for squad in squads_list -%}
    { {% for unit in squad -%}
    "{{ unit }}", {% endfor -%}
    },
    {% endfor -%}
}