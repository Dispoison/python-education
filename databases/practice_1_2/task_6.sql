create or replace function check_rent_date_on_insert()
    returns  trigger
    language plpgsql
as
    $$
    begin
        if new.date != current_date then
            raise exception 'Error: date of renting should be today';
        end if;

        return new;
    end;
    $$;
drop function if exists check_rent_date_on_insert();

create trigger trigger_before_rent_insert
	before insert
	    on rent
	for each row
	execute procedure check_rent_date_on_insert();
drop trigger if exists trigger_before_rent_insert on rent;

select * from rent join car c on rent.car = c.id where rent.id = 1;
insert into rent (date, days, price, customer, car) values ('2018-01-01', 3, 1233, 1, 1);

-- --

ALTER TABLE car ADD COLUMN cost_per_day numeric;

UPDATE car SET cost_per_day = floor(random() * 900 + 100) WHERE cost_per_day IS NULL;


create or replace function increase_price_after_days_update()
    returns  trigger
    language plpgsql
as
    $$
    declare
        car_cost_per_day numeric;
    begin
        select car.cost_per_day into car_cost_per_day from car where car.id = new.car;

        update rent set price = rent.days * car_cost_per_day where rent.car = new.car;
        return new;
    end;
    $$;
drop function if exists increase_price_after_days_update();

create trigger trigger_after_rent_update
	after update
	    of days
	    on rent
	for each row
	execute procedure increase_price_after_days_update();
drop trigger if exists trigger_after_rent_update on rent;

select * from rent join car c on rent.car = c.id where rent.id = 1;
call extend_rent(1, 5);
