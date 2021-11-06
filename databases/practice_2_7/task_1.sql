begin;

create or replace function nullify_order_shipping_total_by_user_city(
    user_city varchar
) returns void
as
$$
    begin
        update orders
        set shipping_total = 0
        where exists(
            select *
            from orders o
            join carts c on c.cart_id = o.cart_id
            join users u on u.user_id = c.user_id
            where u.city = user_city and orders.order_id = o.order_id);

        if not found then
            raise notice'The city "%" could not be found', user_city;
        end if;
    end;
$$ language plpgsql;

SELECT * FROM orders;

SELECT * FROM orders
JOIN carts c on c.cart_id = orders.cart_id
JOIN users u on u.user_id = c.user_id
WHERE u.city = 'city 2';

SELECT * FROM orders
WHERE shipping_total != 0;

do $$
begin
    perform nullify_order_shipping_total_by_user_city('city 2');
    perform nullify_order_shipping_total_by_user_city('city -1');
end; $$;

drop function nullify_order_shipping_total_by_user_city(title varchar);

ROLLBACK;
COMMIT;


-- additionally
BEGIN;

create or replace function get_products_by_category(
    title varchar
) returns products
language sql
as
$$
    select products.*
    from products
    join categories c on c.category_id = products.category_id
    where c.category_title = title
$$;

SELECT * FROM get_products_by_category('Category 2');

drop function get_products_by_category(title varchar);

rollback;
commit;
