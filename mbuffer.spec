Summary:	Measuring Buffer is an enhanced version of buffer
Name:		mbuffer
Version:	20130220
Release:	5
Group:		File tools
License:	GPLv3+
URL:		http://www.maier-komor.de/mbuffer.html
Source0:	http://www.maier-komor.de/software/mbuffer/mbuffer-%{version}.tgz
Patch0:		mbuffer-20121111-pipe-buf.diff
Patch1:		mbuffer-20121111-fix_pointer_cast.diff
BuildRequires:	mt-st
BuildRequires:	mhash-devel

%description
Measuring Buffer is an enhanced version of buffer. It features displayof
throughput, memory-mapped file I/O for huge buffers, and multithreading.

%prep

%setup -q
%patch0 -p0
%patch1 -p0

%build
# suppress detection of MD5_Init functions if openssl-devel
# is available on build system, let only mhash_init be
# detected if the md5 hash feature is enabled
export ac_cv_search_MD5_Init=no

# work around "multi off" in /etc/host.conf and "::1 localhost"
# *not* being the *first* "localhost" entry in /etc/hosts
sed -i 's/localhost:8000/::1:8000/g' Makefile.in

%configure2_5x

%make

%install

%makeinstall_std

%files
%doc AUTHORS ChangeLog LICENSE NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/mbuffer.1*
