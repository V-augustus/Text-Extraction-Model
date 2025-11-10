#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "reproc" for configuration "Release"
set_property(TARGET reproc APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(reproc PROPERTIES
  IMPORTED_IMPLIB_RELEASE "${_IMPORT_PREFIX}/lib/reproc.lib"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/bin/reproc.dll"
  )

list(APPEND _cmake_import_check_targets reproc )
list(APPEND _cmake_import_check_files_for_reproc "${_IMPORT_PREFIX}/lib/reproc.lib" "${_IMPORT_PREFIX}/bin/reproc.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
