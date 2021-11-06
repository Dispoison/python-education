create or replace procedure delete_customer(
    customer_id int)
    as
$$
    declare
        latest_rent_ending date;
    begin
        select max(r.date + r.days * interval '1 days') into latest_rent_ending from customer c
        join rent r on c.id = r.customer
        where c.id = customer_id
        group by c.id;

        if latest_rent_ending < now() then
            delete from customer where id = customer_id;
            commit;
        else
            raise warning 'Error: customer cannot be deleted while the rent is in force';
            rollback;
        end if;
    end;
$$ language plpgsql;

select * from rent where id = 1067;

call delete_customer(1);

drop procedure if exists delete_customer;

-- --

create or replace procedure extend_rent(
    rent_id int,
    days_to_add int)
    as
$$
    declare
        days_before_update integer;
        days_after_update integer;
    begin
        select days into days_before_update from rent where id = rent_id;

        update rent set days = days + days_to_add where id = rent_id;

        select days into days_after_update from rent where id = rent_id;

        if days_after_update > days_before_update then
            commit;
        else
            raise warning 'Error: new days number is lower than old';
            rollback;
        end if;
    end;
$$ language plpgsql;

select * from rent where id = 1;

call extend_rent(1, 4);

drop procedure if exists extend_rent;
