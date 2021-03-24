# OSMPackageConverters

This repo contains scripts for converting OSM release NINE packages to SOL004/SOL007 packages.

## Usage

To run the scripts `osm2sol004` or `osm2sol007` mark them as executables and try them:

```
~$ chmod +x osm2sol004
~$ ./osm2sol004
Usage: osm2sol004 <package_path> <dest_path>
example: osm2sol004 rel9packages/native_charm_vnf new_native_charm_vnf
```

Some OSM release NINE packages are already available at the `rel9packages` folder to quickly test the scripts:

```
~$ ./osm2sol004 rel9packages/native_charm_vnf new_native_charm_vnf
Process completed! SOL004 package available at: new_native_charm_vnf
~$ ls new_native_charm_vnf
ChangeLog.txt  Files  Licenses  native_charm_vnfd.mf  native_charm_vnfd.yaml  Scripts
```

## Additional notes

- The scripts make use of the Apache License already available on this repo. If you want to supply a different license for your converted packages, you can change the `LICENSE_PATH` variable on the scripts.
- Some metadata defaults are assumed by the scripts if those fields are not available at the descriptor level. You may like to edit the generated manifest (`.mf`) file or the package `ChangeLog.txt` after the conversion is completed.
