create or replace procedure cancel_incomplete_orders_by_date_range(
    date_from timestamp without time zone,
    date_to timestamp without time zone)
    as
$$
    declare
        rec orders%rowtype;
        order_status_finished_id integer;
        order_status_canceled_id integer;
    begin
        select order_status_id into order_status_finished_id from order_status where status_name = 'Finished';
        select order_status_id into order_status_canceled_id from order_status where status_name = 'Canceled';
        for rec in
            select * from orders where updated_at between date_from and date_to
        loop
            if rec.order_status_id != order_status_finished_id and rec.order_status_id != order_status_canceled_id then
                update orders set order_status_id = order_status_canceled_id where order_id = rec.order_id;
                update orders set updated_at = now() where order_id = rec.order_id;
            end if;
        end loop;
        commit;
    end;
$$ language plpgsql;

select * from orders
order by updated_at;

select * from orders where updated_at between '2017-01-01' and '2017-01-10';

call cancel_incomplete_orders_by_date_range('2017-01-01', '2017-01-10');

drop procedure if exists cancel_incomplete_orders_by_date_range;

-- -- --

create or replace procedure update_total_in_all_orders()
    as
$$
    declare
        rec record;
        total_in_order numeric;
    begin
        for rec in
            (select orders.* from orders
                join carts c on c.cart_id = orders.cart_id)
        loop
            select sum(p.price) into total_in_order
                from cart_product cp
                join products p on p.product_id = cp.product_id
                where cp.cart_id = rec.cart_id;
            update orders set total = total_in_order where orders.cart_id = rec.cart_id;

            if total_in_order < 0 then
                raise notice 'Total is negative in cart "%"', rec.cart_id;
                rollback;
            end if;
        end loop;
        commit;
    end;
$$ language plpgsql;

select * from orders;

call update_total_in_all_orders();

drop procedure if exists update_total_in_all_orders;