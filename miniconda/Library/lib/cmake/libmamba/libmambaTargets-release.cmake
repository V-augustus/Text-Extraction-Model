#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "mamba::libmamba-dyn" for configuration "Release"
set_property(TARGET mamba::libmamba-dyn APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(mamba::libmamba-dyn PROPERTIES
  IMPORTED_IMPLIB_RELEASE "${_IMPORT_PREFIX}/lib/libmamba.lib"
  IMPORTED_LINK_DEPENDENT_LIBRARIES_RELEASE "reproc;reproc++;simdjson::simdjson;zstd::libzstd_shared"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/bin/libmamba.dll"
  )

list(APPEND _cmake_import_check_targets mamba::libmamba-dyn )
list(APPEND _cmake_import_check_files_for_mamba::libmamba-dyn "${_IMPORT_PREFIX}/lib/libmamba.lib" "${_IMPORT_PREFIX}/bin/libmamba.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
