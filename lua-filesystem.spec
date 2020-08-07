%global commit 8014725009e195ffb502bcd65ca4e93b60a1b21c
# this macro need to be updated with upgrading of lua
%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))" || echo 0)}

Name:           lua-filesystem
Version:        1.6.3
Release:        11
Summary:        File System Library for the Lua Programming Language
License:        MIT
URL:            https://keplerproject.github.io/luafilesystem/
Source0:        https://github.com/keplerproject/luafilesystem/archive/%{commit}/luafilesystem-%{version}.tar.gz

BuildRequires:  gcc lua-devel >= 5.3
Requires:       lua >= 5.3

%description
LuaFileSystem is a Lua library developed to complement the set of functions
related to file systems offered by the standard Lua distribution.

LuaFileSystem offers a portable way to access the underlying directory structure
and file attributes.

%package        help
Summary:        Documents for lua-filesystem
Buildarch:      noarch

%description    help
Man pages and other related documents.

%prep
%autosetup -n luafilesystem-%{commit} -p1

%build
%make_build CFLAGS="%{optflags} -fPIC" PREFIX=%{_prefix} LUA_LIBDIR=%{_libdir}/lua/%{luaver}

%install
make install PREFIX=$RPM_BUILD_ROOT%{_prefix} LUA_LIBDIR=$RPM_BUILD_ROOT%{_libdir}/lua/%{luaver}

%check
LUA_CPATH=$RPM_BUILD_ROOT%{_libdir}/lua/%{luaver}/\?.so lua tests/test.lua

%files
%doc README
%doc doc/us/license*
%{_libdir}/lua/%{luaver}/*

%files help
%doc doc/us/{d,e,i,lua,m}*

%changelog
* Fri Aug 7 2020 shenyangyang <shenyangyang4@huawei.com> - 1.6.3-11
- Add a macro for upgrade of lua

* Fri Nov 29 2019 zhouyihang <zhouyihang1@huawei.com> - 1.6.3-10
- Package init
