%global commit 8014725009e195ffb502bcd65ca4e93b60a1b21c

Name:           lua-filesystem
Version:        1.6.3
Release:        10
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
%make_build CFLAGS="%{optflags} -fPIC" PREFIX=%{_prefix} LUA_LIBDIR=%{_libdir}/lua/5.3

%install
make install PREFIX=$RPM_BUILD_ROOT%{_prefix} LUA_LIBDIR=$RPM_BUILD_ROOT%{_libdir}/lua/5.3

%check
LUA_CPATH=$RPM_BUILD_ROOT%{_libdir}/lua/5.3/\?.so lua tests/test.lua

%files
%doc README
%doc doc/us/license*
%{_libdir}/lua/5.3/*

%files help
%doc doc/us/{d,e,i,lua,m}*

%changelog
* Fri Nov 29 2019 zhouyihang <zhouyihang1@huawei.com> - 1.6.3-10
- Package init
