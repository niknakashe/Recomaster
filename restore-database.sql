-- Restore the RecoMaster database from backup
RESTORE DATABASE RecoMaster
FROM DISK = '/usr/src/app/RecoMaster.bak'
WITH MOVE 'RecoMaster_Data' TO '/var/opt/mssql/data/RecoMaster.mdf',
     MOVE 'RecoMaster_Log' TO '/var/opt/mssql/data/RecoMaster.ldf',
     REPLACE;

-- Create user and grant permissions (optional)
USE RecoMaster;
CREATE USER sa FOR LOGIN sa;
ALTER ROLE db_owner ADD MEMBER sa;
