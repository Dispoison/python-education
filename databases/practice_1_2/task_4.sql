create or replace function count_of_rents_per_branch(
    branch_id int
) returns int as $$
    declare
        count int default 0;
        rec record;
        cur cursor(branch_id int) for select c.branch_id from rent
                                join car c on c.id = rent.car;
    begin
        open cur(branch_id);

        loop
            fetch cur into rec;
            exit when not found;

            if rec.branch_id = branch_id then
                count = count + 1;
            end if;
        end loop;

        close cur;
        return count;
    end;
$$ language plpgsql;

SELECT * FROM count_of_rents_per_branch(50);

drop function count_of_rents_per_branch(branch_id int);

-- --

create or replace function customers_who_rented_car_in_branch(
    branch_id int
) returns table(id int, first_name varchar(255), last_name varchar(255), phone_number varchar(255), address int) as $$
    declare
        rec record;
    begin
        for rec in select distinct c.*, b.id AS branch_id from rent
            join customer c on rent.customer = c.id
            join car cr on cr.id = rent.car
            join branch b on b.id = cr.branch_id
        loop
            if rec.branch_id = branch_id then
                id := rec.id;
                first_name := rec.first_name;
                last_name := rec.last_name;
                phone_number := rec.phone_number;
                address := rec.address;
                return next;
            end if;
        end loop;
        return;
    end;
$$ language plpgsql;

SELECT * FROM customers_who_rented_car_in_branch(12);

drop function customers_who_rented_car_in_branch(branch_id int);
