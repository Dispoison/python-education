create or replace function update_cart_total_on_product_insert()
    returns  trigger
    language plpgsql
as
    $$
    declare
        product_price double precision;
    begin
        select price into product_price from products where products.product_id = new.product_id;
        update carts set total = total + product_price where carts.cart_id = new.cart_id;
        return new;
    end;
    $$;
drop function if exists update_cart_total_on_product_insert();

create trigger trigger_after_insert_cart_product
	after insert
	on cart_product
	for each row
	execute procedure update_cart_total_on_product_insert();
drop trigger if exists trigger_after_insert_cart_product on cart_product;
--
create or replace function update_cart_total_on_product_delete()
    returns trigger
    language plpgsql
as
    $$
    declare
        product_price double precision;
    begin
        select price into product_price from products where products.product_id = old.product_id;
        update carts set total = total - product_price where carts.cart_id = old.cart_id;
        return old;
    end;
    $$;
drop function if exists update_cart_total_on_product_delete();

create trigger trigger_before_delete_product
	before delete
	on cart_product
	for each row
	execute procedure update_cart_total_on_product_delete();
drop trigger if exists trigger_before_delete_product on cart_product;
--
create or replace function update_order_total_on_cart_total_change()
    returns  trigger
    language plpgsql
as
    $$
    begin
        update orders set total = new.total where orders.cart_id = new.cart_id;
        return new;
    end;
    $$;
drop function if exists update_order_total_on_cart_total_change();

create trigger trigger_after_update_cart
	after update
	on carts
	for each row
	execute procedure update_order_total_on_cart_total_change();
drop trigger if exists trigger_after_update_cart on carts;
--

begin;
    select * from products where product_id = 1; -- price - 142.36
    select * from carts where cart_id = 1; -- total - 434.35
    select * from orders where order_id = 1; -- total 434.35
    -- expected 434.35 + 142.36 = 576.71 for both cart and order
    insert into cart_product values (1, 1);
    -- cart(1) and order(1) have 576.71 in total
    delete from cart_product where id = (select last_value from cart_product_id_seq);
    -- cart(1) and order(1) have 434.35 in total
rollback;
commit;
