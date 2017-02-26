DELIMITER //
DROP TRIGGER IF EXISTS after_djangoapp_computers_insert//
CREATE TRIGGER after_djangoapp_computers_insert AFTER INSERT ON djangoapp_computers FOR EACH ROW
BEGIN
	INSERT INTO djangoapp_computersaudit(id, computer_name, IP_address, MAC_address, Operating_system_id, users_name, location, Unit, added_by, timestamp) 
			VALUES(new.id, new.computer_name, new.IP_address, new.MAC_address, new.Operating_system_id, new.users_name, new.location, new.Unit, new.added_by, new.timestamp);
END//
DELIMITER ;


DELIMITER //
DROP TRIGGER IF EXISTS after_djangoapp_computers_update//
CREATE TRIGGER after_djangoapp_computers_update AFTER UPDATE ON djangoapp_computers FOR EACH ROW
BEGIN
	INSERT INTO djangoapp_computersaudit(id, computer_name, IP_address, MAC_address, Operating_system_id, users_name, location, Unit, edited_by, timestamp)
			VALUES(new.id, new.computer_name, new.IP_address, new.MAC_address, new.Operating_system_id, new.users_name, new.location, new.Unit, new.edited_by, new.timestamp);
END//
DELIMITER ;
