# frontend

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


BEGIN;
--
-- Create model Reports
--
CREATE TABLE "app_reports" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "message" text NOT NULL, "user_id" bigint NOT NULL REFERENCES "app_customuser" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "app_reports_VMDGroups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "reports_id" bigint NOT NULL REFERENCES "app_reports" ("id") DEFERRABLE INITIALLY DEFERRED, "vmdgroups_id" bigint NOT NULL REFERENCES "app_vmdgroups" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "app_reports_VMDS" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "reports_id" bigint NOT NULL REFERENCES "app_reports" ("id") DEFERRABLE INITIALLY DEFERRED, "vmds_id" bigint NOT NULL REFERENCES "app_vmds" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "app_reports_user_id_9a2370f3" ON "app_reports" ("user_id");
CREATE UNIQUE INDEX "app_reports_VMDGroups_reports_id_vmdgroups_id_6fb5d686_uniq" ON "app_reports_VMDGroups" ("reports_id", "vmdgroups_id");
CREATE INDEX "app_reports_VMDGroups_reports_id_efbb9672" ON "app_reports_VMDGroups" ("reports_id");
CREATE INDEX "app_reports_VMDGroups_vmdgroups_id_a456799a" ON "app_reports_VMDGroups" ("vmdgroups_id");
CREATE UNIQUE INDEX "app_reports_VMDS_reports_id_vmds_id_c9c28358_uniq" ON "app_reports_VMDS" ("reports_id", "vmds_id");
CREATE INDEX "app_reports_VMDS_reports_id_c736572f" ON "app_reports_VMDS" ("reports_id");
CREATE INDEX "app_reports_VMDS_vmds_id_763a1273" ON "app_reports_VMDS" ("vmds_id");
COMMIT;
