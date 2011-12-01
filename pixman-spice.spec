%define pkgversion 0.13.3
# git b8026d9b7990cf03e3ef7770b04e552ceef89b1d
%define tarversion 0.13.3-git20090127

Name:           pixman-spice
Version:        %{pkgversion}
Release:        5%{?dist}
Summary:        Modified version of pixman for spice

Group:          System Environment/Libraries
License:        MIT
URL:            http://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.bz2
Source0:        pixman-spice-%{tarversion}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# BuildRequires:  automake autoconf libtool pkgconfig

%description
pixman-spice is a pixel manipulation library for X and cairo for Spice.

%package devel
Summary: Pixel manipulation library development package
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
Development library for pixman-spice.

%prep
%setup -q -n pixman-spice-%{tarversion}

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libpixman-spice-1*.so.*

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/pixman-spice-1
%{_includedir}/pixman-spice-1/pixman.h
%{_includedir}/pixman-spice-1/pixman-version.h
%{_libdir}/libpixman-spice-1*.so
%{_libdir}/pkgconfig/pixman_spice-1.pc

%changelog
* Wed Dec  9 2009 Uri Lublin <uril@redhat.com> 0.13.3-5
- Rename package and files from qpixman to pixman-spice

* Thu Apr 23 2009 Soren Sandmann <sandmann@redhat.com> 0.13.3-4
- Rebuild for inclusion in RHEL 5.4.

* Wed Feb 18 2009 Soren Sandmann <sandmann@redhat.com> 0.13.3-3
- Add patch to fix raster op. "or" and "and" were in the wrong order.

* Tue Jan 27 2009 Eduardo Habkost <ehabkost@redhat.com> 0.13.3-2
- Updated to new git snapshot: b8026d9b7990cf03e3ef7770b04e552ceef89b1d

* Thu Jan 8 2009 Soren Sandmann <sandmann@redhat.com> 0.13.3-1
- Header files are called pixman.h, not qpixman.h
- =-=-=-=-=-=-=-=-=- Import QPixman -=-=-=-=-=-=-=-=-=-=

* Tue Nov 18 2008 Dan Williams <dcbw@redhat.com> 0.12.0-2
- Actually build with the altivec detection fix (rh #472000, #451831)

* Wed Sep 17 2008 Soren Sandmann <sandmann@redhat.com> 0.12.0-1
- Upgrade to 0.12.0. Drop stripes patch.

* Wed Sep 10 2008 Soren Sandmann <sandmann@redhat.com> 0.11.10-2
- Add patch to fix stripes in the Nautilus selection retangle.

* Sat Sep 6 2008 Soren Sandmann <sandmann@redhat.com> 0.11.10-1
- Upgrade to 0.11.10. Drop altivec patch.

* Thu Jul 17 2008 Soren Sandmann <sandmann@redhat.com> 0.11.8-1
- Upgrade to 0.11.8. Drop altivec patch.

* Wed Jun 25 2008 Soren Sandmann <sandmann@redhat.com> 0.11.6-1
- Upgrade to 0.11.6. Drop fix for leak.

* Tue Jun 17 2008 David Woodhouse <dwmw2@infradead.org> 0.11.4-3
- Fix Altivec detection breakage (#451831)

* Fri Jun 13 2008 Soren Sandmann <sandmann@redhat.com> 0.11.4-2
- Plug bad leak (cherrypicked from master)

* Mon Jun  9 2008 Soren Sandmann <sandmann@redhat.com> 0.11.4-1
- Update to 0.11.4

* Mon Jun  9 2008 Soren Sandmann <sandmann@redhat.com> 0.11.2-1
- Update to 0.11.2

* Thu Apr  3 2008 Soren Sandmann <sandmann@redhat.com> 0.10.0-1
- Update to 0.10.0

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.6-4
- Autorebuild for GCC 4.3

* Wed Oct 31 2007 Behdad Esfahbod <besfahbo@redhat.com> 0.9.6-3
- Third time's the charm.

* Wed Oct 31 2007 Behdad Esfahbod <besfahbo@redhat.com> 0.9.6-2
- Second try.

* Wed Oct 31 2007 Behdad Esfahbod <besfahbo@redhat.com> 0.9.6-1
- Update to 0.9.6 release.

* Wed Sep 05 2007 Adam Jackson <ajax@redhat.com> 0.9.5-1
- Update to 0.9.5 release.

* Mon Aug 27 2007 Adam Jackson <ajax@redhat.com> 0.9.0-7.20070827
- New snapshot

* Fri Aug 24 2007 Adam Jackson <ajax@redhat.com> 0.9.0-4.20070824
- New snapshot

* Wed Jul 25 2007 Jeremy Katz <katzj@redhat.com> - 0.9.0-3.20070724
- rebuild for toolchain bug

* Tue Jul 24 2007 Adam Jackson <ajax@redhat.com> 0.9.0-2.20070724
- Re-add it, %%dir is not the same as adding a dir whole.

* Tue Jul 24 2007 Adam Jackson <ajax@redhat.com> 0.9.0-1.20070724
- Remove redundant header from %%files devel.

* Fri May 18 2007 Adam Jackson <ajax@redhat.com> 0.9.0-0.20070724
- git build so I can build git X.
